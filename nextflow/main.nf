#!/usr/bin/env nextflow

include { CONVERSION } from './modules/conversion/main.nf'
include { CELLPOSE} from './modules/cellpose/main.nf'
include { METRICS} from './modules/metrics/main.nf'

workflow {
    def channels = params.channels.join(',')
    def ch_images = Channel
        .fromPath(params.input_csv, checkIfExists: true)
        .splitCsv(header:true)
        .map { row ->
            def meta = [:]
            meta.id = row.sample
            def image = file(row.image_path) 
            return [meta, image, channels,params.time_point]
        }
    ch_images.view()
    CONVERSION(ch_images)
    cellpose_input = CONVERSION.out.converted.map { meta, image_files ->
        def cellpose_meta = meta.id ? meta : meta + [id: meta.sample ?: 'sample']
        def model = params.cellpose_model ?: ''
        [cellpose_meta, image_files, model]
    }
    cellpose_input.view()
    CELLPOSE(
            cellpose_input)
    
    ch_metrics = CONVERSION.out.converted
        .combine(CELLPOSE.out.masks, by: 0)
        .map { meta, converted, mask -> tuple(meta, converted, mask, params.properties) } // Join by meta (first element)
    ch_metrics.view()
    METRICS(ch_metrics)
}
