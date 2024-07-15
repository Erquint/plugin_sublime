# [Pieces for Developers](https://pieces.app) | Sublime Plugin

![Pieces Sublime Plugin](icons/hero-image.png)


##### <p align="center"> [Website](https://pieces.app/) • [Pieces OS Documentation](https://docs.pieces.app/) • [Pieces Sublime github repository](https://github.com/pieces-app/plugin_sublime)
</p>

# Important

Please make sure you have [**Pieces OS**](https://docs.pieces.app/installation-getting-started/what-am-i-installing) installed to run the Package.

## Getting Started with the Pieces Sublime Plugin

Welcome to the **Pieces Sublime Plugin**!

The Pieces Sublime plugin is your gateway to managing your saved materials in Pieces directly from within Sublime Text. Seamlessly interact with Pieces OS and enhance your workflow like never before.

## Features
### Configuration

Before diving in, let's ensure everything is set up to your liking. You can customize the LLM model or the host by navigating to:
`Preferences > Package Settings > Pieces > Settings`.
You can also open the settings from the command palette `Pieces: Open Settings`.

### Right Click to Save to Pieces

Saving a new snippet in Pieces is a breeze! Just select the code you want to save, right-click to open the context menu, and choose `Pieces > Save to Pieces`. Your code is now safely stored!

![](https://storage.googleapis.com/pieces_multimedia/PROMOTIONAL/PIECES_FOR_DEVELOPERS/SUBLIME/create.gif)

### Engage with the Pieces Copilot

Ever wished for a personal coding assistant? Look no further! With Pieces Copilot, you can have an AI-powered assistant right at your fingertips. Simply open the command palette and select `Pieces: Copilot`. From there, you can ask anything whether it's for coding help, debugging, or even generating snippets to save to Pieces with some clicks.

![](https://storage.googleapis.com/pieces_multimedia/PROMOTIONAL/PIECES_FOR_DEVELOPERS/SUBLIME/ask%20stream.gif)

### Copilot Ask

Need some help from the Pieces Copilot? Whether it's commenting, fixing a bug, or adding a docstring, just select the code, right-click to open the context menu, and choose `Pieces > Ask Copilot`. Let Copilot do the heavy lifting for you!

![](https://storage.googleapis.com/pieces_multimedia/PROMOTIONAL/PIECES_FOR_DEVELOPERS/SUBLIME/ask.gif)

### Ask about the current Project/File

- **Ask About the Current Project**: Use the command `Pieces: Ask about the current project` to get to be able to ask the Copilot on your Project.
- **Ask About the Current File**: Use the command `Pieces: Ask about the current file` to get the current file that is in focus assistance.

### Sublime Snippet Managment
- **Import Sublime Snippet**: Use the command `Pieces: Import Sublime Snippet` to import a Sublime snippet into Pieces.
- **Export Pieces Material**: Use the command `Pieces: Export Pieces Material` to export a Pieces snippet back to Sublime.

### Open Saved Materials

Ready to access your saved materials? It's super easy! Just follow these steps:

1. Open your command palette (`Ctrl+Shift+P` or `Cmd+Shift+P`).
2. Run the command: `Pieces: Open Saved Material`.
3. Select the asset you wish to open from the list.

Your material is now open and ready for you to use. Happy coding! 

### Edit Saved Materials

Want to make changes to your saved materials? Switch to editor mode by clicking the **Edit** button on your saved snippet. Modify the content as needed and save your changes with a simple `command/ctrl + s`. It's that easy!

![](https://storage.googleapis.com/pieces_multimedia/PROMOTIONAL/PIECES_FOR_DEVELOPERS/SUBLIME/open-edit_snippet.gif)

### Shareable Link

Ever wanted to share a code snippet effortlessly? Select the code, right-click to open the context menu, and choose `Pieces > Generate shareable link`. You can also share a saved material by opening it and clicking the **Share** button. Sharing has never been simpler!

![](https://storage.googleapis.com/pieces_multimedia/PROMOTIONAL/PIECES_FOR_DEVELOPERS/SUBLIME/share.gif)

### [Auto Complete](https://docs.pieces.app/features/code-completion)

Auto-completion of code via snippets to speed up your coding process.If you have saved Pieces Snippets you get automatic completion via Pieces Snippets for specific language. 

you can turn this settings on/off from your settings.
> Open your settings from `Pieces: Open Pieces Settings` and overwrite the `snippet.autocomplete` to false to turn the auto-completion off

### Change the LLM Model

Want to customize your Copilot experience? You can easily switch the LLM model to better suit your needs. Open the settings from your command palette by selecting `Pieces: Open Settings`. You can change some configuration and choose the model that works best for you. Tailor your Copilot to be the perfect coding companion!

### Login/Logout

You can log in and out of your Pieces account using the `Pieces: Login` or `Pieces: Logout` command in your command palette. An output panel is available to check your cloud status and login status.

![](https://storage.googleapis.com/pieces_multimedia/PROMOTIONAL/PIECES_FOR_DEVELOPERS/SUBLIME/auth.gif)

### Connect or Disconnect your Personal Pieces Cloud

You can connect and disconnect from your cloud using `Pieces: Connect Personal Cloud` or `Pieces: Disconnect Personal Cloud` command in your command palette.
Note: In order you use these commands, you must have an account connected to Pieces.

### Find your Saved Materials

You can search a saved material using `Pieces: Search`.

There are three main types of seaching:

- **Fuzzy Search**: Fuzzy Search is a technique used to find matches that are likely to be relevant, even if they are not exact matches. It is particularly useful for handling typos, misspellings, and variations in data.

- **Full Text Search**: Full Text Search is a technique used to search for documents or records that contain the exact sequence of words in the search query. It indexes all the words in a document to enable fast and efficient searching.

- **Neural Code Search**: Neural Code Search is a technique that leverages neural networks and machine learning to improve the search and retrieval of code snippets. It allows you to use natural language to describe what you are looking for, capturing the semantics and context of the code to provide more accurate and relevant results.

![](https://storage.googleapis.com/pieces_multimedia/PROMOTIONAL/PIECES_FOR_DEVELOPERS/SUBLIME/search.gif)

### Reload the Plugin

If you're experiencing an issue or something isn't working properly, try reloading the plugin using the command `Pieces: Reload Plugin` in your command palette. Don't forget to make sure Pieces OS is running.

### Get Support or Share Feedback

Experiencing an issue or have feedback for the Pieces team? No worries, we've got you covered. Simply open the command palette and run `Pieces: Get Support`. From here, you will find resources where you can connect with the Pieces team.

## How to install?

### Stable build (Recommended):

- Download the [package control](https://packagecontrol.io/installation)
- Open your command palette. You can use the shortcut key combination `Ctrl+Shift+P` on Windows and `Cmd+Shift+P` on MacOS.
- Search for `Package Control: Install Package`  
- Search for Pieces and select it.
> IMPORTANT: When you first download the package, it will download and install some required dependencies. As a result, you might need to restart Sublime after installing.

### Pre-releases:

You can download and checkout some new beta features before releasing.

- Make sure you have downloaded the [package control](https://packagecontrol.io/installation)
- Download the `Pieces.sublime-package` from [releases](https://github.com/pieces-app/plugin_sublime/releases) on GitHub 
- Add `Pieces.sublime-package` to the Installed Packages directory.
	- **Windows**: %APPDATA%\Sublime Text\Installed Packages
	- **MacOS**: ~/Library/Application Support/Sublime Text 3/Installed Packages
	- **Linux**: ~/.config/sublime-text/Installed Packages
- Open Sublime and enjoy the package


## Connect with the Pieces Community

#### Join our [Discord Community](https://discord.gg/getpieces)

Become a part of our Discord community to stay updated and engage in discussions about our features.

#### Submit a Feature Request or Feedback

Have an idea for a new feature? Feel free to submit your suggestions on our [GitHub page](https://github.com/pieces-app/plugin_sublime/issues).

#### Tech Blogs

Stay connected and up-to-date with our latest [blogs](https://code.pieces.app/blog).

#### Plugins

Explore our collection of awesome Pieces [plugins](https://code.pieces.app/plugins).

#### View Power Tips & Best Practices

Don't forget to check out our YouTube channel for [Power Tips & Best Practices](https://youtube.com/@getpieces)


### Privacy and Data Collection

We take your privacy seriously. We are committed to ensuring that your data remains private and secure. To that end, we want to make it clear that:

**We do not collect any client side telemetry.**

[Read more about data collection and privacy](https://docs.pieces.app/product-highlights-and-benefits/privacy-security-data)

