wget https://www.robots.ox.ac.uk/~vgg/data/oxbuildings/oxbuild_images-v1.tgz

mkdir data
tar -xvf oxbuild_images-v1.tgz -C data
rm -f oxbuild_images-v1.tgz

echo "Format data"
python format_data.py --data_path data

echo "Prepare CSV"
python prepare_data_csv.py --data_path data --output_path data 