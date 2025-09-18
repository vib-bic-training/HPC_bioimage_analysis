process CONVERSION {
    label 'convert'
    
    input:
    tuple val(meta), path(image), val(channels), val(time_point)

    output:
    tuple val(meta), path("*.ome.tiff"), emit: converted
    path "versions.yml", emit: versions

    script:
    """
    mkdir -p converted
    convert_czi2ometiff.py --image_path ${image} --output_dir ./converted --channels ${channels} --time_point ${time_point}
    
    # Move output files to current directory for proper publishing
    mv converted/*.ome.tiff ./ || true
    
    cat <<-END_VERSIONS > versions.yml
    "${task.process}":
        python: \$(python --version | sed 's/Python //g')
    END_VERSIONS
    """
    
    // stub:
    // """
    // touch ${meta.id}_metrics.xlsx
    
    // cat <<-END_VERSIONS > versions.yml
    // "${task.process}":
    //     python: \$(python --version | sed 's/Python //g')
    // END_VERSIONS
    // """
}
