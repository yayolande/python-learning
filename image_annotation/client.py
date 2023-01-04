
import imageToAnnotation
import annotationToDish
import dish


imagePath = input(" Enter the food image path to get information : ")
imagePath = imagePath.strip()

annotation = imageToAnnotation.getAnotation(imagePath)
dish = annotationToDish.getDish(annotation)

print(dish)