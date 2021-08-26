<h1 align = 'center'>CSGO Sticker Capsule Data Analysis</h1>

  As an avid CSGO player and fan, I've noticed a consistently positive trend regarding the price of CSGO sticker capsules. It's a fairly well known fact in the CSGO community that these capsules gain value over time, but I wanted to know how quickly and reliably I could expect growth before investing my hard earned money. Over the past year I've delved into the world of investment, learning as much as I can, and making plenty of speculative mistakes in the process. I decided to combine my interests, and gain valuable experience in data exploration and analysis with this project.

<h2>Table of Contents</h2>
<details open>
<summary>Show/Hide</summary>
<br>

1. [ About CSGO, Sticker Capsules, and the Steam Market ](#about)
2. [ File Descriptions ](#file_desc)
3. [ Technologies Used ](#tech)
4. [ Structure ](#Structure)
5. [ Executive Summary ](#Executive_Summary)
   * [ 1. Webscraping, Early EDA, and Cleaning ](#Webscraping_Early_EDA_and_Cleaning)
       * [ Webscraping ](#Webscraping)
       * [ Early EDA and Cleaning](#Early_EDA_and_Cleaning)
   * [ 2. Further EDA and Preprocessing ](#Further_EDA_and_Preprocessing) 
   * [ 3. Modelling and Hyperparameter Tuning ](#Modelling)
   * [ 4. Evaluation ](#Evaluation)
       * [ Future Improvements ](#Future_Improvements)
   * [ 5. Neural Network Modelling ](#Neural_Network_Modelling)
   * [ 6. Revaluation and Deployment ](#Revaluation)
</details>

<h2>About CSGO, Sticker Capsules, and the Steam Market</h2>
<details>
<a name="about"></a>
<summary>Show/Hide</summary>
<br>

  Counter-Strike: Global Offensive (abbreviated to CSGO) is a first-person shooter game developed by Valve. The earliest iteration of the Counter-Strike series was created in 2000, and over many years the franchise has built up a massive global fanbase. CSGO is designed to be played competitively, and the highest level of competition has seen significant growth over the past decade. It's now one of the most popular esports in the world, with the biggest events attracting hundreds of thousands of online viewers.
  
  Every year, Valve parters with tournament organizers to host two major events. As a way to increase fan interaction and raise money for the players, Valve sells $1 virtual sticker capsules for the durantion of the event. When opened, the user recieves a random sticker of a team logo or player autograph from a pool of possible stickers, depending on the type of capsule. These stickers can be applied to a user's weapon to increase its "cool factor," for lack of a better word. Multiple types of stickers can drop from the same capsule, including regular, holographic, foil (shiny), and gold stickers. Teams and players have a wide range of popularity in the CSGO scene, and generally more popular players have higher valued stickers. Following the conclusion of an event, Valve sells the capsules at a heavily discounted price of $0.25 for about a week, before the offer is permanently removed. As a result, unopened capsules become scarce and the price of rare stickers rises.

  The platform that allows these capsules to have value is the Steam Market. Steam is owned by Valve, and is the most popular place to buy PC games. Valve has implemented a marketplace where players can buy and sell items from many games, allowing virtual items to have cash value. While Steam does not allow users to directly cash out their balance, third party websites make use of the trading system to set up cash exchanges. Players trade their items to bots, which then trade the items to buyers. After nearly a decade of devlopment, the Steam Market has created a thriving economy based solely on virtual items.
  
</details>

