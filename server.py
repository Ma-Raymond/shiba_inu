from google_images_download import google_images_download

response = google_images_download.googleimagesdownload()
arguments = {"keywords":"shiba inu",
             "limit":10,"print_urls":False}
paths = response.download(arguments)

print(paths)