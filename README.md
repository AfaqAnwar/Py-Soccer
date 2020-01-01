# Py-Soccer-AI
An "AI" (sort-of) that I made when I was bored that can play the Soccer Messenger game!

## The Method
* Capture game screen.
* Convert to the specified range of rgb color.
* Downscale it by a resize factor.
* Find the soccer ball (first pixel with a color value that is > 0)
* Move mouse and click it.

### Flaws
* Inaccuracy dependent upon resize factor.
* Speed.

_The speed is an issue which is dependent upon the resize factor. If we were to process the full game image it could be very precise but would take way too long to actually find and click the proper pixel due to the rapid nature of the game._

## Running Script Locally

### Requirements for Hosting Locally
I recommend you install Anaconda and create a virtual Python environment, this is the simplest and cleanest way to get any python project with requirements running locally.

[Anaconda Documentation](https://docs.anaconda.com/anaconda/)

I also reccomend finding a trustable Android emulator, the one I used was [MEmu](https://www.memuplay.com/).

### Prerequisites
```
    MEmu - or any comparative Arnoid emulator that can run Messenger.
    
    Python 3.6.X

    capture
    
    cv2
    
    wxPython
    
    pywin32
    
    numpy
```

### Steps
  1. Clone this repository onto your local machine.
  
  2. Edit ```Py-Soccer-AI/run.py``` to include the window name of your emulator. Default is MEmu.
  
  *  Edit ```Py-Soccer-AI/run.py``` to view the game only with no extra ui elements if using a different emulator other than MEmu.
  
  3. Run run.py 
 
#### Warning: Since this is an experimental project, I have not implemented a fail safe. In the event your mouse is uncontrollable, a system restart may be required. This is a quick fix, but I have no plans on advancing this project further.
