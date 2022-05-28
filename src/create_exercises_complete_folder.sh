#!/bin/bash
rm -rf ../build/export

mkdir ../build/export
mkdir ../build/export/exercises
mkdir ../build/export/correction
mkdir ../build/export/exercises/examples
mkdir ../build/export/correction/examples
mkdir ../build/export/project

cp intro_python_exercise_correction.ipynb ../build/export/correction/intro_python_exercise_correction.ipynb
# TODO: add the version without correction
cp truc.py ../build/export/exercises/truc.py
cp truc.py ../build/export/correction/truc.py
cp examples/TD6_Exam_MCQ.csv ../build/export/exercises/examples/TD6_Exam_MCQ.csv
cp examples/TD6_Exam_MCQ.csv ../build/export/correction/examples/TD6_Exam_MCQ.csv

cp ../build/Project.pdf ../build/export/project/Project.pdf
cp masse-salariale-et-assiette-chomage-partiel-mensuelles-du-secteur-prive_modif.csv ../build/export/project/masse-salariale-et-assiette-chomage-partiel-mensuelles-du-secteur-prive_modif.csv
