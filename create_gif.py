import imageio.v3 as iio

filenames = [
    'team-pic1.png', 
    'team-pic2.png'
    ]
fileNameBase = ""

amount = 0

images = []

print("please make sure that the pictures you want to use follow the correct naming convention: name1.png")
fileNameBase = input("What is the name of your photo? without the number and the .png " )
amount = input(f"how many photos are there from which the name starts with {fileNameBase} ")

for filename in filenames:
    images.append(
        iio.imread(
            filename
        )5
    )

iio.imwrite(
    'team.gif', 
    images, 
    duration = 500, 
    loop = 0
)

