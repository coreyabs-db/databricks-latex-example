# Databricks notebook source
# MAGIC %md
# MAGIC This notebook installs the minimal packages needed to run pdflatex from Databricks.

# COMMAND ----------

!apt-get update -y && apt-get install -y texlive-base texlive-binaries texlive-extra-utils
