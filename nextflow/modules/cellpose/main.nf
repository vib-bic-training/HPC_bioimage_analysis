process CELLPOSE {
    label 'cellpose'  
    input: 
    tuple val(meta), path(image_tiles), val(cellpose_model)

    output:
    tuple val(meta), path("*.tif"), emit: masks
    path "versions.yml", emit: versions
    
    script:
    def args = task.ext.args ?: ''
    def model_command = cellpose_model ? "--pretrained_model $cellpose_model" : ""
    """
    mkdir -p output
    cellpose_seg_nextflow.py --image_path $image_tiles --output_dir ./output $model_command $args
    mv output/*.tif ./ || true
    cat <<-END_VERSIONS > versions.yml
    "${task.process}":
        python: \$(python --version | sed 's/Python //g')
    END_VERSIONS
    """
}
