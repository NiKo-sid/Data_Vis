def convert_dat_to_raw(input_file, output_file):
    try:
        with open(input_file, 'rb') as dat_file, open(output_file, 'wb') as raw_file:
            raw_file.write(dat_file.read())  
        print(f"Conversion successful: {output_file}")
    except Exception as e:
        print(f"Error during conversion: {e}")

input_dat = "/Users/sidkid/Downloads/Conversion/stagbeetle832x832x494.dat"
output_raw = "highres.raw"

convert_dat_to_raw(input_dat, output_raw)
