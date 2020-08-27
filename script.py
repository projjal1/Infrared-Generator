import sys
import numpy as np
import cv2
import matplotlib as mpl
import matplotlib.cm as mtpltcm

def main(argv):
    cap = cv2.VideoCapture(1)

    while (True):
        # Capture frame-by-frame
        ret, frame = cap.read()

        # Our operations on the frame come here
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        #initialize the colormap (jet) to get infrared 
        #one can also use cool or viridis_r colorMap for lighter or dark background
        colormap = mpl.cm.jet
        
        #add a normalization
        cNorm = mpl.colors.Normalize(vmin=0, vmax=255)
        #init the mapping
        scalarMap = mtpltcm.ScalarMappable(norm=cNorm, cmap=colormap)

        colors = scalarMap.to_rgba(gray)
        cv2.imshow('frame', colors)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    sys.exit(main(sys.argv))