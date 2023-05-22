# Databricks notebook source
# MAGIC %md
# MAGIC This notebook shows how to compile a latex document to a PDF using pdflatex and then easily download it with a link.
# MAGIC
# MAGIC First, you need to install texlive. You can do that either via a cluster init script (see cluster-init.sh) or within a notebook (see install-texlive-from-notebook). 
# MAGIC
# MAGIC This example only installs the minimal requirements. If you need more, consider installing texlive-full instead, but be aware that it is rather large.

# COMMAND ----------

# MAGIC %md
# MAGIC Once the libraries are installed, you just run pdflatex, or whatever other latex build you need.

# COMMAND ----------

!pdflatex example.tex

# COMMAND ----------

# MAGIC %md
# MAGIC Once you compile it, you may want to download it. In that case, you can copy it to the FileStore directory and then create a download link.

# COMMAND ----------

import os
import tempfile

filestore_dir = "/dbfs/FileStore/"
export_dir = tempfile.TemporaryDirectory(dir=filestore_dir, prefix="temp-pdf-export-")
temp_dir_name = export_dir.name.removeprefix(filestore_dir)

# COMMAND ----------

!cp example.pdf {export_dir.name}/example.pdf

# COMMAND ----------

displayHTML(f"""<a href="files/{temp_dir_name}/example.pdf">example.pdf</a>""")

# COMMAND ----------

# MAGIC %md
# MAGIC When you're all done, cleanup the temp directory.

# COMMAND ----------

export_dir.cleanup()
