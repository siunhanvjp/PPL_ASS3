start_num = 300
end_num = 400

with open("temp.txt", "w") as f:
    for num in range(start_num, end_num+1):
        
        res = f"""
        
        def test_{num}(self):
            input = \"\"\"
                
                    \"\"\"
            expect = "[]"
            self.assertTrue(TestChecker.test(input, expect, {num}))
        
        """
        
        f.write(res)