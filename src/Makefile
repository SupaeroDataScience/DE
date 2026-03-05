REMOTE ?= origin

all:
	mkdocs build
	cd reveal; reveal-md . \
        --template static/template/reveal.html \
        --listing-template static/template/listing.html \
        --css static/css/evo.css \
        --css static/css/reset.css \
        --static-dirs static \
        --static ../site/slides

serve-site:
	cd reveal; rm -r ../docs/slides; reveal-md . \
        --template static/template/reveal.html \
        --listing-template static/template/listing.html \
        --css static/css/evo.css \
        --css static/css/reset.css \
        --static-dirs static \
        --static ../docs/slides

	mkdocs serve

serve-slides: 
	cd reveal; reveal-md . \
        --template static/template/reveal.html \
        --disable-auto-open \
        --css static/css/evo.css \
        --css static/css/reset.css \
        --static-dirs static

sync:
	bash sync.sh

deploy:
	# 1. Build mkdocs site into site/
	mkdocs build
	# 2. Build slides directly into site/slides/
	cd reveal; reveal-md . \
        --template static/template/reveal.html \
        --listing-template static/template/listing.html \
        --css static/css/evo.css \
        --css static/css/reset.css \
        --static-dirs static \
        --static ../site/slides
	# 3. Deploy everything in one push (no checkout needed)
	ghp-import -n -p -r $(REMOTE) -b gh-pages site

clean:
	rm -rf site
	rm -rf docs/slides
