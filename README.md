This project is a web application that allows users to vote for their preferred candidates in an election. It employs MongoDB for database management which features three collections: candidates, elections, and users.

Installation and Setup : MongoDB To set up the required database collections, refer to the files in /server/Models after adding the URL in line 2 of /server/.env.

Third-Party Email Verification: For automatic email sending, configure third-party verification for your email and register the app to obtain a secret key. Then, add the email and password details to /server/.env. To get pass key, visit Google Support.

Ganache: Install Ganache to receive free Ethereum. Add the configuration in /smart_contract/truffle-config.js to your account to receive ten free accounts with 100 ETH each.

MetaMask: Install the MetaMask Chrome extension to manage transactions.

Contract Compilation: To compile the contract, open the command prompt and navigate to the smart_contract directory using cd smart_contract. Run npm install -g truffle (if Truffle is not already installed), then execute truffle compile and truffle migrate. After compilation, follow the instructions to copy and paste the address and transaction.json.

After installing Ganache, compile the contract in the smart_contract directory using Truffle. Add the transaction address to Client/utils/Constant.js. Additionally, copy smart_contract/build/contracts/Transaction.json and paste it into Client/utils/Transaction.json for the ABI value.

Python Script (for face authentication): Install the necessary packages using pip install opencv-python numpy os face_recognition. Add photos to the /Face directory with the corresponding usernames. To specify the photo URL, modify line 6 in /server/Controller/encoded.py.

#If you encounter any issues in installing face_recognition package, try installing the dlib manually by the given file named as (dlib-19.24.99-cp312-cp312-win_amd64.whl) And also if still you facing issues, try to lower the version of numpy.

Running the Web Application: To run the web application, follow these steps: open a terminal and Go to the client folder, install all node modules using npm install, and then run npm run start. open second terminal and Go to the server folder, install all node modules using npm install, and then run nodemon main. Wait a few minutes for the site to start.

#make sure you are going to Client or client, change in one letter might get you an error. Case-sensitive.

Libraries to be installed:

npm install -g truffle
pip install opencv-python
pip install face_recognition
