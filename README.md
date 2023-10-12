# Computational Education Research Lab at MSU

This is the website for the Computational Education Research Lab at Michigan State University.

## Building the website locally
In order to work on the website locally so that you can check if things are rendering correctly before you push them to GitHub, you need to do a install few things. For mac users, this guide overall seems to be the most useful for getting things up and running: https://jekyllrb.com/docs/installation/macos/ (for other OS users, you can check the corresponding guide here: https://jekyllrb.com/docs/installation/).

But basically it boils down to making sure you have the following installed:

* Ruby
    * If you’re on a Mac, the easiest option is problem to install this with Homebrew. For GitHub pages, they need to be built with Ruby 2.7 (which is pretty out of date at this point), so you’ll want to do `brew install ruby@2.7`. Info on this issue is here: https://github.com/github/pages-gem/issues/752
    * Originally, I found these two resources are probably useful, but they recommend different ways of install ruby and will result in installing newer versions of Ruby, which won’t work. I’m keeping them for posterity:
https://www.ruby-lang.org/en/documentation/installation/#homebrew
https://jekyllrb.com/docs/installation/macos/
    * For other operating systems, it might be useful to start here (know that as a Mac user, I cannot attest to any of this as actually functioning!): https://jekyllrb.com/docs/installation/ or here: https://www.ruby-lang.org/en/documentation/installation/

* Jekyll
    * Should be able to install with `gem install jekyll` once you have Ruby installed and functional

* Bundler
    * Should be able to do `gem install bundler`

Once you get these things installed, you should be able to clone the repo (https://github.com/msu-cerl/msu-cerl.github.io). Then when you’re in that directory, just run to build it locally:
```
bundle install
bundle exec jekyll serve
```
When you’re working in the repo and making changes to update the website, generally speaking you shouldn’t have to commit anything in the “_” folders (e.g. _site) to the GitHub repo because GitHub pages will build and deploy those files once you push new changes (though this process takes a few minutes).

Let me know if you run into issues when working with the website. If you have content you’d like to have featured on the website, but would rather not go down the path of updating the repo yourself, just send that along to me and I’ll get it up there.
