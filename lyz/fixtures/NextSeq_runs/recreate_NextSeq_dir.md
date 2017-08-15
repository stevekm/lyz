find 170809_NB501073_0019_AH5FFYBGX3/ -type f ! -name "*.jpg" ! -name "*.bcl*" ! -name "*.fastq*" ! -path "*.git/*" ! -path "*demultiplexing-stats/*" ! -path "*Unaligned/Reports/html/*" ! -path "*InterOp/*" ! -path "*/RTALogs/*" ! -path "*/Recipe/*" ! -path "*/Logs/*" ! -path "*/Config/*" ! -path "*/L00*" ! -path "*old/*" ! -path "*/qsub_logs/*" | while read item; do touch "./lyz/fixtures/NextSeq_runs/${item}"; done
rsync -vah --exclude="*.git/*" --include="*/" --exclude="*"  ../../../../quicksilver/170809_NB501073_0019_AH5FFYBGX3 NextSeq_runs/
cp ../170809_NB501073_0019_AH5FFYBGX3/RTAComplete.txt  fixtures/NextSeq_runs/170809_NB501073_0019_AH5FFYBGX3/