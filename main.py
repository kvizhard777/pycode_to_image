from pytoimage import PyImage
from pathlib import Path

def pycode_to_img(file_path = 'main.py'):
	path = Path(file_path)

	if not path.is_file():
		return 'Oops... please, check a file path'

	code = PyImage(file_path, background = (20, 20, 20))  # Background color (RGB)
	palette = {
		'line': (255, 255, 255),   # Number color (RGB)
		'normal': (255, 255, 255)  # Letter color (RGB)
	}

	code.set_color_palette(palette = palette)
	code.generate_image()
	img_name = f'{file_path.split(".")[0]}.png'
	code.save_image(img_name)

	return f'{img_name} saved sucessfully!'

def main():
	file_path = input("Please, enter a file name: ")  # File name
	print(pycode_to_img(file_path = file_path))

if __name__ == '__main__':
	main()