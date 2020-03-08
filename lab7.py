from pylab import *
import mahotas
from PIL import *

Im = array(Image.open("led.jpg"))

subplot(1,2,1)
imshow(Im)
ImHSV = matplotlib.colors.rgb_to_hsv(Im)
H=ImHSV[:,:,0]
S=ImHSV[:,:,1]
V=ImHSV[:,:,2]

figure(2)
subplot(1,4,1);imshow(H);subplot(1,4,2);imshow(S);subplot(1,4,3);imshow(V);
#M=(S>0.6)*(H>0.5) #cat
#M=(S>0.14)*(H<0.145) #highway
#M=(S>0.3)*(H<0.05) #tomato
#M=(S<0.155)*(H>0.55) #cloud bug
#M=(S < 0.1)*(H > 0.4) * (V > 0.5) #led
M=(1)*(1)*(V == 255) 
subplot(1,4,4);imshow(M ,cmap='gray'); 
figure(1)
subplot(1,2,2);imshow(dstack((M*Im[:,:,0],M*Im[:,:,1],M*Im[:,:,2])));
show()


