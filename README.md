# RTSP streaming using GStreamer

Python implementation to stream camera feed from OpenCV videoCapture via RTSP server using GStreamer 1.0.

## Installation

This implementation has been developed and tested on Ubuntu 16.04 and 18.04. So the installation steps are specific to debian based linux distros.

### Step-1 Install GStreamer-1.0 and related plugins
    sudo apt-get install libgstreamer1.0-0 gstreamer1.0-plugins-base gstreamer1.0-plugins-good gstreamer1.0-plugins-bad gstreamer1.0-plugins-ugly gstreamer1.0-libav gstreamer1.0-tools gstreamer1.0-x gstreamer1.0-alsa gstreamer1.0-gl gstreamer1.0-gtk3 gstreamer1.0-qt5 gstreamer1.0-pulseaudio
### Step-2 Install RTSP server
    sudo apt-get install libglib2.0-dev libgstrtspserver-1.0-dev gstreamer1.0-rtsp
### Step-3 dependecy for pyobjects
    sudo apt-get install -y libgirepository1.0-dev gir1.2-gstreamer-1.0 gobject-introspection
    sudo apt-get install -y build-essential meson ninja-build
### Requirement
- Python 3.x
- Opencv 3.x or above ( pip install opencv-python )
- pygobject

### Usage
> Run stream.py with required arguments to start the rtsp server
##### Sample 
    python stream.py --device_id 0 --fps 30 --image_width 640 --image_height 480 --port 8554 --stream_uri /video_stream
    
### Visualization

You can view the video feed on `rtsp://server-ip-address:8554/stream_uri`

e.g: `rtsp://192.168.1.12:8554/video_stream`

You can either use any video player which supports rtsp streaming like VLC player or you can use the `open-rtsp.py` script to view the video feed.


# Streaming RTSP Over the Internet Using Ngrok

This README explains how to stream a local RTSP feed over the internet using Ngrok. The guide includes steps to set up Ngrok for TCP tunneling.

## Prerequisites

- Ngrok installed on your machine.
- A running RTSP server on port 8554.

## Steps

### 1. Download and Install Ngrok

- Download Ngrok from the official website: [https://ngrok.com/download](https://ngrok.com/download).
- Extract and install Ngrok on your machine by adding it to the system PATH.

### 2. Start an Ngrok Tunnel for RTSP

To forward the RTSP server port over the internet, run the following command in your terminal:

```bash
ngrok tcp 8554
```

This command will establish a TCP tunnel to port 8554, providing a public URL such as `tcp://x.tcp.ngrok.io:xxxxx`.

### 3. Access the Public RTSP Stream

Once the Ngrok tunnel is running, your RTSP stream will be available via the public URL:

```bash
rtsp://x.tcp.ngrok.io:xxxxx/video_stream
```

You can use VLC Media Player or Python OpenCV to view the RTSP stream from any internet-connected device.

## Notes

- **Ngrok Free Plan Limitation**: The free plan has a time limit, so the session will need to be restarted periodically.
- **Keep Ngrok Running**: Ngrok must be kept running to maintain the public RTSP tunnel.
- **Stability and Latency**: The stability and latency of the RTSP stream might be affected by your internet speed and region.

## Security Considerations

- Add user authentication to the RTSP server to prevent unauthorized access.
- Consider using a VPN or a secure tunnel to enhance encryption and security.

