# import required modules
from keras.models import load_model
import numpy as np
import cv2, time

wait = time.sleep

# use a keras model to make a prediction and show that to the user
def show_prediction(model, data, choice):
    # ask the model to make a prediction
    pred = model.predict(data)[0]
    # sort the prediction from largest to smallest
    psort = np.argsort(pred)[::-1]
    # show the user all the predictions
    print(*["{} - {: 6.2f}%,".format(choice[x], 100*pred[x]) for x in psort], end="\r")
    # return the most likely choice
    return psort[0]

# use the camera to select rock, paper, or scissors
def get_rock_paper_scissor(model, capture):
    choice = ["Rock", "Paper", "Scissors", "None"]
    selected = _selected = 3
    # keep looping until we have an image
    while True:
        # create the numpy array for the image ( 224x224 pixels )
        data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
        # fetch an image
        _, frame = capture.read()
        # resize the image to 224 x 224 pixels.
        image = np.array(cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA))
        # and normalise the image to between 0 and 127
        normalised_image = (image.astype(np.float32) / 127.0) - 1
        # add the normalised image to the data array
        data[0] = normalised_image
        # show the user what the model thinks has been chosen
        selected = show_prediction(model, data, choice)
        # show the user the image
        cv2.imshow("Press [ Q ] to select", frame)
        # if the user selected q, then quit
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    # remind the user of their choice (also hide the updating bit)
    print("You have chosen {}{}".format(choice[selected], " "*50))
    # return the selection
    return selected

# play a round of rock paper scissors
def play_round(model, capture):
    # define the three outputs
    outputs = ["Rock", "paper", "Scissors"]
    # select the computers choice
    computer_choice = np.random.randint(0, 3)
    # fetch the users choice
    user_choice = get_rock_paper_scissor(model, capture)
    # show the user the responses
    print("Computer: {}\nYou:      {}\n".format(outputs[computer_choice], outputs[user_choice]))
    # compare the responses
    result = (computer_choice - user_choice) % 3
    # determine who won!
    if result == 0:
        # the round is a draw if they chose the same
        print("That round was a draw!")
        return np.array([0, 0])
    elif result == 1:
        # the computer won if it chose the answer to the right of the user in our cyclic set
        print("The computer won that round!")
        return np.array([1, 0])
    else:
        # the user won if it chose the answer to the left of the computer in our cyclic choice set
        print("You won that round!")
        return np.array([0, 1])

# main program script
def main(model, capture):
    # track the cumulative score, stored as an array of [comp, user]
    score = np.array([0, 0])
    # track the win condition
    win_score = 0
    # ask the user to select the wining score
    while win_score < 1:
        try:
            # fetch the users choice
            win_score = int(input("At what score should a winner be declared?\n> "))
        # if they didn't choose a valid integer, this exception block will catch it
        except:
            print("That was not a valid choice I'm afrad")
    # add a break to the output
    print()
    # while noone has won the game, loop
    while not win_score in score:
        # play a round and fetch the score
        score += play_round(model, capture)
        # show the score
        print("The current score is:\nComputer: {}\nYou:      {}\n".format(*score))
    # determine which part of the score array has a win condition
    winner = np.where(score==win_score)[0][0]
    # tell the user if they have won or not
    print("{}, you have {} the game!".format("Congratulations" if winner else "Commiserations",
                                             "won" if winner else "lost"))

# ensure this is the top level script
if __name__ == "__main__":
    # fetch the neural network
    model = load_model("source/keras_model/keras_model.h5")
    # start the video capture
    capture = cv2.VideoCapture(0)
    # execute the main program script
    main(model, capture)
    # once we have finished, stop capturing video
    capture.release()
    # and remove the video capture window
    cv2.destroyAllWindows()