(defstruct joueur
  x
  y
  zap-count
  has-zap)

(defstruct dalek
  x
  y)

(defparameter *x* 20 "Taille en X de l'arene")
(defparameter *y* 20 "Taille en Y de l'arene")
(defvar *daleks* ())
(defvar *joueurs* (make-joueur :x (random *x*) :y (random *y*)))

(defun dalek-deplacement (dalek joueur)
  (cond
    ((> (dalek-x dalek) (joueur-x joueur)) 
     (decf (dalek-x dalek)))
    ((< (dalek-x dalek) (joueur-x joueur)) 
     (incf (dalek-x dalek))))
  (cond
    ((> (dalek-y dalek) (joueur-y joueur)) 
     (decf (dalek-y dalek)))
    ((< (dalek-y dalek) (joueur-y joueur)) 
     (incf (dalek-y dalek)))))

;; (setf (dalek-y dalek) (+ (joueur-y joueur) 1)))))

(defun init-dalek (n)
  (loop for i from 1 to n
       do (push (make-dalek :x (random *x*) :y (random *y*)) *daleks*)))

(defun deplace-daleks ()
  (loop for i in *daleks*
       do (dalek-deplacement i *joueurs*)))

