default: install

all: install build


h help:
	@grep '^[a-z]' Makefile


i install:
	bundle config set --local path vendor/bundle
	bundle install

u upgrade:
	bundle update

s serve:
	bundle exec jekyll serve --trace --livereload

b build:
	JEKYLL_ENV=development bundle exec jekyll build --trace