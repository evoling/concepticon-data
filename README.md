# Concepticon-Data

[![Build Status](https://travis-ci.org/clld/concepticon-data.svg?branch=master)](https://travis-ci.org/clld/concepticon-data)

This repository offers the raw data underlying the [Concepticon](http://concepticon.clld.org) of the [CLLD](http://clld.org) project. Here, you can find [previous and latest releases](https://github.com/clld/concepticon-data/releases), [current issues we are trying to handle](https://github.com/clld/concepticon-data/issues), as well as the [most actual unreleased form of the data](https://github.com/clld/concepticon-data/tree/master/concepticondata).

Further information you may find here and which you may find interesting:

* For an overview on the status of all currently linked conceptlists, see [here](https://github.com/clld/concepticon-data/blob/master/concepticondata/conceptlists/README.md).
* For basic information on metadata, see [here](https://github.com/clld/concepticon-data/blob/master/concepticondata/concept_set_meta/README.md).
* For information on how you can contribute to the project or profit from the data sources we offer, see [here](https://github.com/clld/concepticon-data/blob/master/CONTRIBUTING.md).


## Data Structure

- **conceptlists/** folder contains conceptlists with links to IDs in concepticon.tsv, the 
  lists are named after the first person who proposed them, the year of the reference publication 
  in which we extracted them, and the number of concepts. All these three parts of information 
  are separated by a dash. Furthermore, in cases where two lists would have an identical name, 
  we add alphabetical letters to the lists to distinguish them. Files need to have the columns 
  "GLOSS" (some still have "ENGLISH" instead, but this needs to be changed), additionally, most 
  (if not all files) have a "NUMBER" field indicating the number in the reference, which is also 
  important for ordering the entries as given in the original source. Additional columns are more 
  or less free to the user, but we tried to be consistent.
- **conceptlists.tsv** contains metadata about the lists in **conceptlists/**.
- **references/references.bib** the bibtex file showing links to all concept lists (bibtex-key 
  identical to the name of the conceptlist file, without file-ending. File further contains links 
  to the references  in which the conceptlists were published (references stored in the "crossref" field). 
- **sources/** contains pdf-files of each conceptlist (only the list-parts, not the full publications 
  for copyright reasons), naming is the same as for the conceptlists, but with the ending ".pdf" instead of ".tsv".
- **concepticon.tsv** the backbone concept list. All concepts from individual concept lists are linked to entries in this file.
- **concept_set_meta/** contains lists of metadata, relating concept sets to additional information, e.g. on Wikipedia. 
  These lists are described by accompanying metadata files following the recommendations of the 
  [Model for Tabular Data and Metadata on the Web](http://www.w3.org/TR/tabular-data-model/).



