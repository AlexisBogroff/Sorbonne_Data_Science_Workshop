# Course on Financial Engineering with Python, Linux and Git

This course is made up of:
* 6 one-hour-and-a-half-long lectures
* 5 three-hour-long tutorials with correct version
* 1 one-hour-long multiple-choice questionnaire with correct version

It has initially been given on Q1 2021 at Ecole Supérieure d'Ingénieurs Léonard de Vinci (ESILV) to master students.

It could easily be reused and presented to any Engineering School or University.  
It could also be presented internally to newcomers at Horizon.

## Directory content

* The **build** directory contains the whole course: lectures, tutorials, questionnaire and correct versions.
* The **src** directory contains the tex source files as well as some tutorial correct versions as code snippets.
* The **images** directory contains all images (mostly vector graphics), material and tools to create them.
* The **data** directory contains downloaded and computed data for the tutorials.

## Build the whole course

The slides and tutorials are written in Latex.

The code snippets depend on the **minted** Latex package that in turn depends on the **Pygments** external python library.
Check that Latex and Pygments are correctly installed on your system.

The whole course can be built using the command:
```
source build_all.sh
```

Individual lecture or tutorial can be built from the **src** directory with the command:
```
source build.sh [TEXFILE]
```

It takes roughly 5 minutes to build the whole course.  
Output will be found in the **build** directory.  
Corresponding logs will be found in the generated **logs** directory.

## Build the vector graphics

Most images are generated as vector graphics.
You need to install different tools and check that corresponding binaries are correctly set in you system's path:
* pdfseparate (to select one page in an existing pdf)
* pdfcrop (to crop pdf empty margins)
* batik (to transform svg to pdf)
* graphviz (to generate graphs)
* plantuml (to generate uml diagrams)

Example of required commands can be found in the different bash scripts found in the **images/work** subdirectory.
