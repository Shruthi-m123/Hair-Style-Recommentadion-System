#classified_shape=""
#def shape1(k):
#    this.classified_shape=k;
#def shape():
#    return classified_shape
import User_Input as img_path
import User_Point as img_points
ans=img_points.user_points(img_path.selected_file_path)
import Code1 as pdt
k=pdt.prediction(ans)
def shape():
    return k
