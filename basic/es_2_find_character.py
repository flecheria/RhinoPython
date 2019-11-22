from time import clock

if __name__ == "__main__":
    
    # time at the beginning of the script
    start = clock()
    
    # simple test
    # test = "ksdkghk"
    # complex test
    # test = "ksdghfkasjdhlfkjasdgkfjsgsdlfasdkfgjsdgueeryueteiuewibbiewubcuweiuciweuviuwyeoiut"
    # very complex test
    test = '''kjgsl gmuwieynpwekjgsl gmuwieynpwegupginpoigybuyoypuakjgkjhzx,nxmn
              bzxmcoiyuiqwerurqwuyiuqewrioyuiucvucbmnbmnbzxxhcfjhgfasjkfglqwliuy
              hfewjh lgh liugl iaer liy grl blv lirbu liarbglrahliu la l iuh liu
              alu hl auerh uha o uh ivkjzcxagfxhtasgregxwezhvtdfhctresxgzregaqre
              zgqtrdwjzytdqjytdvjzqzeqpkfnfhnmlkgldfkjhlibj ldij lbdfhk uhsdv ku
              hku  ghe iuhiuh iygkuf ut ktyfkz tfqkwuyfk quwygfk uykjgsl gmuwiey
              npwegupginpoigybuyoypuakjgkjhzx,nxmnbzxmcoiyuiqwerurqwuyiuqewrioyu
              iucvucbmnbmnbzxxhcfjhgfasjkfglqwliuy hfewjh lgh liugl iaer liy grl
              blv lirbu liarbglrahliu la l iuh liualu hl auerh uha o uh ivkjzcxa
              gfxhtasgregxwezhvtdfhctresxgzregaqrezgqtrdwjzytdqjytdvjzqzeqpkfnfh
              nmlkgldfkjhlibj ldij lbdfhk uhsdv kuhku  ghe iuhkjgsl gmuwieynpweg
              upginpoigybuyoypuakjgkjhzx,nxmnbzxmcoiyuiqwerurqwuyiuqewrioyuiucvu
              cbmnbmnbzxxhcfjhgfasjkfglqwliuy hfewjh lgh liugl iaer liy grl blv 
              lirbu liarbglrahliu la l iuh liualu hl auerh uha o uh ivkjzcxagfxh
              tasgregxwezhvtdfhctresxgzregaqrezgqtrdwjzytdqjytdvjzqzeqpkfnfhnmlk
              gldfkjhlibj ldij lbdfhk uhsdv kuhku  ghe iuhiuh iygkuf ut ktyfkz t
              fqkwuyfk quwygfk uyiuh iygkuf ut ktyfkz tfqkwuyfk quwygfk uygupgin
              poigybuyoypuakjgkjhzx,nxmnbzxmcoiyuiqwerurqwuyiuqewrioyuiucvucbmnb
              mnbzxxhcfjhgfasjkfglqwliuy hfewjh lgh liugl iaer liy grl blv lirbu
              liarbglrahliu la l iuh liualu hl auerh uha o uh ivkjzcxagfxhtasgre
              gxwez<hvtdfhctresxgzregaqrezgqtrdwjzytdqjytdvjzqzeqpkfnfhnmlkgldfk
              jhlibj ldij lbdfhk uhsdv kuhku  ghe iuhiuh iygkuf ut ktyfkz tfqkwu
              yfk quwygfk uy'''
    
    # character to find
    char = 'k'
    
    # TODO break after first if

    if(char in test):
        print("I found " + str( test.count(char) ) + " characters")
        result = []
        
        
        # version 1
        # best time 5.02 msec - worst time 8.43
        for i in range( len(test) ):
            
            if(test[i] == char):
                result.append(i)
        
        
        """
        # version 2
        # best time 2.9 msec - worst time 5.62
        pos = 0
        for i in range( test.count(char) ):
            
            # DEBUG
            # a = test[pos:]
            # print(a)
            
            id = test[pos:].index(char)
            # print("pos: %s" % (pos) )
            # print("id : %s" % (id) )
            result.append(pos + id)
            
            pos += (id + 1)
        """
        
    else:
        print("no way")
    
    # result
    # [x, y, z, ...]
    print(result)
    
    # time when script ends
    print("Execution time: %s msec" % ( round(clock() - start, 5) * 1000 ) )