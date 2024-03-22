# MAT4400-LinnAnaly
Notes for MAT4400-Linear analysis. The notes are taken from Measures, Integrals and Martingales and from the lectures. 
## Usage:
All files should be saved with the same structure/in the same place as similar files. E.g. **Ch_16_subfile.tex** and **Ch_13_subfile.tex** in the folder **Chapter_Files**. Some lectures are not from Measures, Integrals and Martingales, they are saved in the folder **Appendix** or **Stand_Alone_Lectures**. 

NB! The folder **TMP** should not be deleted, it is needed for **create_subfiles.py**.

##### MAT4400_notes.tex
Comment out "\detailedfalse" on line $$\sim$$117 to switch between the detailed version of the notes. Elements that are not considered as important in the notes (such as proofs in some cases) can be placed on the form:
```latex
\ifdetailed
this is not as important
\fi
```
and they will be excluded depending on if "\detailedfalse" is commented out or not.

Question: *Should we rearrange and structure the n-th chapters in **MAT4400_notes.tex** as the n-th lecture instead?*

##### Python files (may need update to work for windows):
* create_subfiles.py: 
    - Creates seperate .tex and .pdf files for each chapter/lecture/appendix stored in the Chapters_Files, Stand_Alone_Lectures or Appendix folder respectively. Stores these pdfs in the folder PDFs.
    - Deletes all .tex and all auxiliary files
* delete_auxiliary_fields.py:
    - Deletes all auxiliary files