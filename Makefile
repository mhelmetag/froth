clean:
	@rm -f data/images/*.png
	@rm -f ml/images/*.{png,json}
	@rm -f ml/labels/*.png

compress-data:
	@tar -czf data/images/images.tar.gz data/images/*.png
	@tar -czf ml/images/images.tar.gz ml/images/*.png ml/images/*.json
	@tar -czf ml/labels/labels.tar.gz ml/labels/*.png

decompress-data:
	@tar -xzf data/images/images.tar.gz
	@tar -xzf ml/images/images.tar.gz
	@tar -xzf ml/labels/labels.tar.gz

start-labelme:
	@labelme ml/images --labels ml/codes.txt --nodata

.PHONY: clean compress-data decompress-data start-labelme
