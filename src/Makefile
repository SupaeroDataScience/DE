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
	git checkout master
	mkdocs gh-deploy
	cd reveal; reveal-md . \
        --template static/template/reveal.html \
        --listing-template static/template/listing.html \
        --css static/css/evo.css \
        --css static/css/reset.css \
        --static-dirs static \
        --static ../../slides
	mv ../slides ../slides_new
	git checkout gh-pages
	rm -rf ../slides
	mv ../slides_new ../slides
	git add ../slides
	git commit -m "Updated reveal slides"
	git push origin gh-pages
	git checkout master

clean:
	rm -rf site
	rm -rf ../slides
	rm -rf ../slides_new
