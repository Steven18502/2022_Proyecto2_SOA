import schedule
import time
from google.cloud import vision 
from google.cloud import storage

# Constants
apikey = "./app/apikey.json"
bucketname = "soa-vision-bucket"

# [START vision_face_detection_gcs]
def detect_emotions_cloud():
  """Detects faces in the file located in Google Cloud Storage or the web."""

  # Activate Google vision API using service account key
  client = vision.ImageAnnotatorClient.from_service_account_json(apikey)
  
  # Get GCS bucket
  storage_client = storage.Client.from_service_account_json(apikey)
  bucket = storage_client.bucket(bucketname)
  
  # Get images paths (only one MUST be in bucket)
  blob_list = list(bucket.list_blobs())
  
  # Check if there
  if not blob_list:
    print("Bucket is empty")
    return False
  
  # List to save records
  records = []
  
  # how many images to analyze
  n = 3
  # Analize n blobs from the list
  for i in range(0, n):
    
    # when index become bigger than the list
    if len(blob_list) < (i+1):
      break
    
    # Get blob name
    blob_name = blob_list[i].name
    print(f"Image - {i+1}")
    print(f"Blob: {blob_name} analize.")
    
    # Build image path
    image_path = "gs://{0}/{1}".format(bucketname, blob_name)

    # [START vision_python_migration_image_uri]
    image = vision.Image()
    image.source.image_uri = image_path
    # [END vision_python_migration_image_uri]

    # API face detection response
    response = client.face_detection(image=image)
    
    # Face expression detection
    faces = response.face_annotations

    # Names of likelihood from google.cloud.vision.enums
    likelihood_name = ('UNKNOWN', 'VERY_UNLIKELY', 'UNLIKELY', 'POSSIBLE','LIKELY', 'VERY_LIKELY')
    
    
    # # Get emotions of all faces
    # emotions_json = []
    # if faces:
    #   for index, face in enumerate(faces):
    #     emotions = []
    #     emotions.append(index+1)
    #     emotions.append(likelihood_name[face.joy_likelihood])
    #     emotions.append(likelihood_name[face.sorrow_likelihood])
    #     emotions.append(likelihood_name[face.anger_likelihood])
    #     emotions.append(likelihood_name[face.surprise_likelihood])
    #     emotions_json.append(emotions)
    #     show(emotions)
    #     records.append(emotions_json)
    
    # Get emotions of the first face (default)
    if faces:
      face = faces[0]
      emotions = []
      emotions.append(likelihood_name[face.joy_likelihood])
      emotions.append(likelihood_name[face.sorrow_likelihood])
      emotions.append(likelihood_name[face.anger_likelihood])
      emotions.append(likelihood_name[face.surprise_likelihood])
      show(emotions=emotions)
      records.append(emotions)
    
    # Delete the analyzed image.
    # delete_blob(bucket, blob_name)
    
    if response.error.message:
        raise Exception(
            '{}\nFor more info on error messages, check: '
            'https://cloud.google.com/apis/design/errors'.format(
                response.error.message))
      
  return [True, records]
# [END vision_face_detection_gcs]


def delete_blob(bucket, blob_name):
  """Deletes a blob from the bucket."""
  blob = bucket.blob(blob_name)
  blob.delete()
  print(f"Blob: {blob_name} deleted.")

# Function that prints the emotion to the terminal.
# INPUT: emotions array.
# OUTPUT: print the values with respective labels.
def show(emotions):
  print()
  print('joy: {}'.format(emotions[0]))
  print('sorrow: {}'.format(emotions[1]))
  print('anger: {}'.format(emotions[2]))
  print('surprise: {}\n'.format(emotions[3]))


# Function that handles the routine.
def routine():
    # After every x seconds.
    schedule.every(10).seconds.do(detect_emotions_cloud)
    
    # Every 30  or 00:00 time.
    # schedule.every().day.at("00:00").do(detect_emotions_cloud)
    
    # Loop
    while True:
      schedule.run_pending()
      time.sleep(1)