import sys, os
from contextlib import contextmanager

class Stand_alone_subfiles:

    def __init__(self, default_tex="TMP/_default.tex", save_to_folder="", read_from="", delete_tex=False):

        self._after_title_txt = r"\maketitle" + "\n" + r"\date" + "\n"
        self._end_txt = r"\end{document}"
        with open(default_tex, "r") as file:
            self._start_txt = file.readlines()

        self._save_to_folder = save_to_folder
        self._delete_tex = default_tex
        if read_from != "":
            read_from = read_from + "/"
        self._read_from = read_from
        self._subfile_names = []

    def create_stand_alone_texes(self, sandwich=["Ch_","_subfile.tex"], iterable=range(1,29)):
        for i in iterable:
            msg = ""
            try:
                filename_read = f"Ch_{i}_subfile.tex"
                filename_read = self._read_from + sandwich[0] + str(i) + sandwich[1]
                
                with open(filename_read, "r") as file:
                    txt = file.readlines()
                
                n1 = txt[0].index(r"{"); title = ""
                j = 1
                while txt[0][n1 + j] != "}":
                    title += txt[0][n1 + j]
                    j += 1
                            
                filename_write = f"Ch_{i}_{title}.tex"
                filename_write = sandwich[0] + str(i) + f"_{title}.tex"

                filename_write = filename_write.replace(r"\(", ""); filename_write = filename_write.replace(r"\)", "")
                filename_write = filename_write.replace(r"$", ""); filename_write = filename_write.replace(" ", "_")
                filename_write = filename_write.replace("-", "_"); filename_write = filename_write.replace("\\", "")
                
                msg = f"Created {filename_write} successfully"; to_save = filename_write
                if self._save_to_folder != "":
                    filename_write = filename_write
                    msg = msg + f"at {self._save_to_folder}"

                with open(filename_write, "w") as file:
                    for j in range(len(self._start_txt)):
                        file.write(self._start_txt[j])
                    
                    middle_text = r"\begin{document}" + "\n"
                    try:
                        int(i)
                        middle_text += r"\setcounter{section}{" + f"{i}" + "}\n"
                        middle_text += r"\setcounter{theorem}{" + f"{i}" + "}\n"
                    except:
                        continue
                    
                    file.write(middle_text)
                    file.write(r"\title{" + title + "}\n")
                    file.write(r"\author{Morten Tryti Berg and Isak Cecil Onsager Rukan. }" + "\n")
                    file.write(self._after_title_txt)
                    for j in range(1, len(txt)):
                        file.write(txt[j])
                    file.write("\n" + self._end_txt)

                self._subfile_names.append(to_save)

                print(msg)
            except:
                continue

    def create_pdfs(self):
        location = ""; Move = False
        if self._save_to_folder != "":
            location = self._save_to_folder + "/"
            move = True

        for i in range(len(self._subfile_names)):
            os.system("pdflatex " + f'"{self._subfile_names[i]}"')
            os.system("pdflatex " + f'"{self._subfile_names[i]}"')

            if move:
                os.system("mv " +  f'"{self._subfile_names[i][0:-3]}pdf" ' + location + f'"{self._subfile_names[i][0:-3]}pdf"')
            
            if self._delete_tex:
                os.system("rm " f'"{self._subfile_names[i]}"')
                
    def delete_auxiliary_fields(self):
          with open(".gitignore", "r") as file:
            for line in file:
                if line[0] == "*":
                    delete_this = line[1:].strip()
                    os.system(f"rm *{delete_this}")


@contextmanager
def suppress_stdout():
    with open(os.devnull, "w") as devnull:
        old_stdout = sys.stdout
        sys.stdout = devnull
        try:  
            yield
        finally:
            sys.stdout = old_stdout

if __name__ == "__main__":
    kjoor = Stand_alone_subfiles(save_to_folder="PDFs", read_from="Chapters_Files", delete_tex=True)
    kjoor.create_stand_alone_texes()
    kjoor._read_from = "Appendix/"
    # kjoor.create_stand_alone_texes(sandwich=["Appendix_", "_subfile.tex"], iterable=["H"])
    kjoor.create_stand_alone_texes(sandwich=["Appendix_", "_subfile.tex"], iterable=["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", 
                                                                  "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"])
    kjoor._read_from = "Stand_Alone_Lectures/"
    kjoor.create_stand_alone_texes(sandwich=["lecture", "_subfile.tex"])

    kjoor.create_pdfs()
    kjoor.delete_auxiliary_fields()