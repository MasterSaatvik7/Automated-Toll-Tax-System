# IoT-Based Indian License Plate Recognition System

This project demonstrates an IoT-based license plate recognition system. It integrates object detection and optical character recognition (OCR) to identify license plates from video frames, validate them, and send SMS notifications to registered phone numbers. MongoDB is used for storing vehicle details, and Twilio is used for SMS functionality.

## Features
- **Object Detection**: Uses the FCOS (Fully Convolutional One-Stage) model to detect license plates.
- **License Plate Recognition (LPR)**: Recognizes and decodes license plate numbers using an LPRNet model.
- **Database Integration**: Connects to a MongoDB database to validate license plates.
- **SMS Notifications**: Sends toll payment notifications via Twilio to registered users.
- **Real-Time Video Processing**: Processes frames from a video file or real-time camera feed.

## Directory Structure
```
IoT
├── Indian_LPR
│   ├── IoTproj.py         # Main script
│   ├── weights            # Model weights
│   │   ├── best_od.pth    # Weights for object detection model
│   │   ├── best_lprnet.pth # Weights for LPRNet model
│   ├── src
│       ├── object_detection
│       │   ├── model
│       │   │   ├── fcos.py
│       │   │   ├── config.py
│       │   ├── utils
│       │       ├── utils.py
│       ├── License_Plate_Recognition
│           ├── model
│           │   ├── LPRNet.py
│           ├── test_LPRNet.py
│
├── jsons
│   ├── output.json        # Processed frame outputs
```

## Prerequisites

Before running the project, ensure the following dependencies are installed:

- Python 3.8+
- OpenCV
- PyTorch
- MongoDB
- Twilio Python SDK
- tqdm

Install the required packages using:

```bash
pip install -r requirements.txt
```

## Setting Up

### 1. Add Twilio Credentials

Update the following placeholders in `IoTproj.py` with your Twilio account details:

```python
account_sid = 'AddYourCredentialsHere'
auth_token = 'AddYourTokenHere'
twilio_number = '+PutYourTwilioNumberHere'
```

### 2. MongoDB Connection

Replace `MongoDB_URL` with your MongoDB connection string:

```python
uri = "MongoDB_URL"
```

### 3. Download Model Weights

Ensure the model weights `best_od.pth` and `best_lprnet.pth` are present in the `weights` directory.

### 4. Add Vehicle Data

Insert vehicle license plate data and associated phone numbers into the MongoDB collection. An example document:

```json
{
    "lcn": "TN22BB1234",
    "phn": "9876543210"
}
```

## Usage

### Running the Script

Run the script using the following command:

```bash
python IoTproj.py
```

### Input Video

Update the video file path in `process_video`:

```python
current_video = cv2.VideoCapture("./170609_A_Delhi_026.mp4")
```
Set it to `0` for real-time camera feed.

### Output

- Annotated video frames with detected license plates and their labels.
- JSON output saved to `./jsons/output.json`.
- SMS notifications sent to registered phone numbers.

### Quit

Press `q` to quit the video processing loop.

## Code Flow

1. **Object Detection**: Detects license plates in video frames.
2. **License Plate Recognition**: Extracts and decodes license plate numbers.
3. **Database Lookup**: Validates detected plates with MongoDB entries.
4. **SMS Notification**: Sends toll payment link to the vehicle's registered owner.

## Example Output

- **Detected License Plate**: TN22BB1234
- **SMS Sent To**: +911234567890
- **Processed JSON**: 

```json
{
    "0": {
        "0": {
            "boxes": [10, 20, 110, 50],
            "label": "TN22BB1234"
        }
    }
}
```

## Notes

- Make sure MongoDB and Twilio credentials are correctly set up.
- Modify the SMS body text as needed.
- Supported state codes for Indian license plates are hardcoded in the script.

## Acknowledgments

This project uses the `Indian_LPR` library, which is based on the work from the following repository:  
[https://github.com/sanchit2843/Indian_LPR](https://github.com/sanchit2843/Indian_LPR)

I would like to acknowledge and thank the contributors of this repository for providing the foundational code and models used in this project.


## License
This project is open-source and available under the MIT License.

---

Feel free to reach out with any questions or issues!
