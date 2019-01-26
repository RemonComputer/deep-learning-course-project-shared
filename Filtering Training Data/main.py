import os
import shutil

import pandas as pd





if __name__ == '__main__':

    input_folder = '../Dataset'
    train_folder_name = 'train'
    train_labels_file_name = 'train.csv'
    output_folder = 'output'

    imgaes_input_folder_path = os.path.join(input_folder, train_folder_name)
    images_output_folder_path = os.path.join(output_folder, train_folder_name)

    os.makedirs(images_output_folder_path, exist_ok=True)
    train_dataframe = pd.read_csv(os.path.join(input_folder, train_labels_file_name))
    Images = []
    Ids = []
    target_whale_ids = ['w_1287fbc',
                        'w_98baff9',
                        'w_7554f44',
                        'w_1eafe46',
                        'w_fd1cb9d',
                        'w_693c9ee',
                        'w_ab4cae2',
                        'w_73d5489',
                        'w_3674103',
                        'w_ab6db0f',
                        'w_c0cfd5b',
                        'w_b729b1f']

    for (_,(ImageFileName, WhaleId)) in train_dataframe.iterrows():
        if WhaleId in target_whale_ids:
            Images.append(ImageFileName)
            Ids.append(WhaleId)
            input_file_path = os.path.join(imgaes_input_folder_path, ImageFileName)
            output_file_path = os.path.join(images_output_folder_path, ImageFileName)
            shutil.copyfile(input_file_path, output_file_path)

    output_dataframe  = pd.DataFrame({'Image':Images, 'Id':Ids})
    output_df_file_path = os.path.join(output_folder, train_labels_file_name)
    output_dataframe.to_csv(output_df_file_path, index=False)

