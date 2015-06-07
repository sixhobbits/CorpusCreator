# Corpus Creator

## Goals

An all-in-one corpus creator and manager allowing for 
* Crawling sites using RSS, Internet Archive, or live crawling
* Crawling comments on new articles
* Boilerplate removal and plaintext extraction
* Dedupliation
* Metadata extraction
* Post-processing, including POS tagging
* KWIC (Key word in context) view
* Collocates
* More

This was a project I did research on for my honours degree (see dwyer.co.za/thesis). I am planning to slowly cleanup/rewrite the code base (in a private repo) and move the modules here.

The project currently runs on an Ubuntu server using MongoDB, Apache2, Flask, and various Python libraries, including NLTK. The design is kept as modular as possible with the idea that various components, such as the tagger, deduplicator, or boilerplate remover should be easily replaceable should alternatives be required.
