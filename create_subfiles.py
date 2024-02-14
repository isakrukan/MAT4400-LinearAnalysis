import os

class Stand_alone_subfiles:

    def __init__(self, default_tex="TMP/_default.tex", save_to_folder="", delete_tex=False):

        self._after_title_txt = r"\maketitle" + "\n" + r"\date{}" + "\n"
        self._end_txt = r"\end{document}"
        with open(default_tex, "r") as file:
            self._start_txt = file.readlines()

        self._save_to_folder = save_to_folder
        self._delete_tex = default_tex

    def create_stand_alone_texes(self):
        self._subfile_names = []
        for i in range(1,29):
            try:
                filename_read = f"Ch_{i}_subfile.tex"
                with open(filename_read, "r") as file:
                    txt = file.readlines()
                
                n1 = txt[0].index(r"{"); title = ""
                j = 1
                while txt[0][n1 + j] != "}":
                    title += txt[0][n1 + j]
                    j += 1
                            
                filename_write = f"Ch_{i}_{title}.tex"

                filename_write = filename_write.replace(r"\(", ""); filename_write = filename_write.replace(r"\)", "")
                filename_write = filename_write.replace(r"$", ""); filename_write = filename_write.replace(" ", "_")
                filename_write = filename_write.replace("-", "_"); filename_write = filename_write.replace("\\", "")
                
                msg = f"Created {filename_write} successfully"; to_save = filename_write
                if self._save_to_folder != "":
                    filename_write = self._save_to_folder + "/" + filename_write
                    msg = msg + f"at {self._save_to_folder}"

                with open(filename_write, "w") as file:
                    for j in range(len(self._start_txt)):
                        file.write(self._start_txt[j])
                    
                    middle_text = r"\setcounter{section}{" + f"{i}" + "}\n"
                    middle_text += r"\setcounter{theorem}{" + f"{i}" + "}\n"
                    middle_text += r"\begin{document}" + "\n"
                    
                    file.write(middle_text)
                    file.write(r"\title{" + title + "}\n")
                    file.write(self._after_title_txt)
                    for j in range(1, len(txt)):
                        file.write(txt[j])
                    file.write(self._end_txt)

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
            os.system("pdflatex " + location + f'"{self._subfile_names[i]}"')
            os.system("pdflatex " + location + f'"{self._subfile_names[i]}"')
            if move:
                os.system("mv " +  f'"{self._subfile_names[i][0:-3]}pdf" ' + location + f'"{self._subfile_names[i][0:-3]}pdf"')
            
            if self._delete_tex:
                os.system("rm " + location + f'"{self._subfile_names[i]}"')
                
    def delete_auxiliary_fields(self):
          with open(".gitignore", "r") as file:
            for line in file:
                if line[0] == "*":
                    delete_this = line[1:].strip()
                    os.system(f"rm *{delete_this}")

if __name__ == "__main__":
    kjoor = Stand_alone_subfiles(save_to_folder="Chapters", delete_tex=True)
    kjoor.create_stand_alone_texes()
    kjoor.create_pdfs()
    kjoor.delete_auxiliary_fields()