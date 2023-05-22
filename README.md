# databricks-latex-example

This is a simple example which shows how to compile latex documents on Databricks environment.

It's basically the same as compile latex on any normal environment, but you may also want to generate a simple download link for your resulting PDF document.

To install the relevant texlive pieces, you can use either a cluster init script to install across the cluster, or just use a `%sh` or `!` command to install on the driver. An example init script is in `cluster-init.sh` and an example installation notebook is in `install-texlive-from-notebook`.

Once that's complete, an example of compiling tex to pdf is given in the `compile-latex-example` notebook. It also shows how to generate a download link for your pdf in a temp directory.
