# Merge conflicts occur when 2 people make different changes to one location in a file.

# For example, if I write "x=5" on line 6 in my local repo, but my collaborator already pushed her changes that said "x=10" on line 6 to the remote repo,
# when I push my changes, Git will not know which version to keep, and will result in a merge conflict

x=1234

# Another way merge conflicts can occur is if you merge your branch with another, but there are differences between the branches that Git cannot resolve