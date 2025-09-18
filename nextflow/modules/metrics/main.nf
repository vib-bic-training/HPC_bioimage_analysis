process METRICS {
    label 'metrics'
        
    input:
    tuple val(meta), path(image), path(mask), val(properties)

    output:
    tuple val(meta), path("*.xlsx"), emit: metrics
    path "versions.yml", emit: versions

    script:
    def args = task.ext.args ?: ''
    """
    mkdir -p output_metrics
    metrics.py --image_path ${image} --output_dir ./output_metrics --label_path ${mask} --properties ${properties} $args
    
    # Move output files to current directory for proper publishing
    
    mv output_metrics/*.xlsx ./ || true
    
    cat <<-END_VERSIONS > versions.yml
    "${task.process}":
        python: \$(python --version | sed 's/Python //g')
    END_VERSIONS
    """
    
    stub:
    """
    touch ${meta.id}_metrics.xlsx
    
    cat <<-END_VERSIONS > versions.yml
    "${task.process}":
        python: \$(python --version | sed 's/Python //g')
    END_VERSIONS
    """
}
