default: install

all: install build

RUN_JEKYLL = bundle exec jekyll serve

h help:
	@grep '^[a-z]' Makefile

i install:
	bundle config set --local path vendor/bundle
	bundle install

u upgrade:
	bundle update

ds dev-serve:
	JEKYLL_ENV=development $(RUN_JEKYLL)

ls live-serve:
	JEKYLL_ENV=production $(RUN_JEKYLL)

b build:
	bundle exec jekyll build --trace