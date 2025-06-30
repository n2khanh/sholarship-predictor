from sklearn.metrics import r2_score,mean_squared_error
import matplotlib.pyplot as plt

# Functions for evaluating model
def evaluate_model(y_pred , Y_test):
    mse = mean_squared_error(y_pred=y_pred,y_true=Y_test)
    r2 = r2_score(y_pred= y_pred , y_true = Y_test )
    print("Mean squared error : {mse}" )
    print("R2_score : {r2}"  )

    #Plot to compare 
    plt.figure(figsize=(6, 6))
    plt.scatter(Y_test, y_pred, alpha=0.6, color='blue')
    plt.plot([0, 1], [0, 1], 'r--')  #  y = x
    plt.xlabel('Actual Scholarship Probability')
    plt.ylabel('Predicted')
    plt.title('Actual vs Predicted')
    plt.grid(True)
    plt.show()
    return mse,r2