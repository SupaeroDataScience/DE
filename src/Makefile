REMOTE ?= origin
SOURCE_BRANCH ?= main

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
	git checkout $(SOURCE_BRANCH)
	# deploy site
	mkdocs gh-deploy -r $(REMOTE) -b gh-pages
	# build slides
	cd reveal; reveal-md . \
        --template static/template/reveal.html \
        --listing-template static/template/listing.html \
        --css static/css/evo.css \
        --css static/css/reset.css \
        --static-dirs static \
        --static ../../slides_new
	# commit them to gh-page branch
	git checkout gh-pages
	rm -rf ../slides
	mv ../slides_new ../slides
	git add ../slides
	git commit -m "Updated reveal slides"
	# push to gh-pages
	git push $(REMOTE) gh-pages
	# re-checkout current branch
	git checkout $(SOURCE_BRANCH)

clean:
	rm -rf site
	rm -rf docs/slides
	rm -rf ../slides
	rm -rf ../slides_new
