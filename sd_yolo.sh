search_dir=stable_diffusion_results
for entry in "$search_dir"/*
do
  echo "$entry"
  ./darknet detect cfg/yolov3.cfg yolov3.weights $entry >> sd_output_log.txt
done

