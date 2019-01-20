# create a class
class Solution:
    #class attributes
    """ none """
    # instance attibutes

    emails = {"alice.a@leetcode.com", "bob+bob@leetcode.com", "alice.bob@leetcode.com"}

    def __init__(self, emails):
        seen = set()
        for email in emails:
            local, domain = email.split("@")
            if '+' in local:
                local = local[:local.index('+')]
            seen.add(local.replcae('.', '') + '@' + domain)
        return(len(seen))
        
