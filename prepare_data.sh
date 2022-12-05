echo "Format data"
python format_data.py --data_path data

echo "Prepare CSV"
python prepare_data_csv.py --data_path data --output_path data 