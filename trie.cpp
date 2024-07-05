#include<bits/stdc++.h>
using namespace std;
class TrieNode
{
    public:
    char ch;
    bool islast=false;
    vector<TrieNode*> children;
    TrieNode() 
    {}
    TrieNode(char ch)
    {
        this->ch=ch;
        for(int i=0; i<26; i++)
        {
            TrieNode* r=NULL;
            this->children.push_back(r);
        }
        this->islast=islast;
    }
};
bool insert(TrieNode* root,string key)
{
    if(!root)
        return false;
    TrieNode* run = root;
    // cout<<root->ch-'a'<<"hi"<<endl;
    for(int i=0; i<key.size(); i++)
    {
        int index = key[i]-'a';
        // cout<<index<<"---"<<endl;
        // cout<<run->children[index]<<endl;
        if(!run->children[index])
        {
            run->children[index] = new TrieNode(key[i]);
        }
        run = run->children[index];
    }
    run->islast = true;
    // cout<<root->ch<<endl;
    return true;
}
bool search(TrieNode* root,string key)
{
    if(!root)
        return false;
    TrieNode* run  = root;
    if(key[0]!=run->ch)
        return false;
    for(int i=1; i<key.size(); i++)
    {
        int index = key[i]-'a';
        if(!run->children[index])
            return false;
        run=run->children[index];
    }
    return true;
}
int size_l(TrieNode* root)
{
    int ans=0;
    for(auto e: root->children)
    {
        if(e)
            ans++;
    }
    return ans;
}
bool delete_word(string key,TrieNode* root,int length,int run)
{
    if (!root)
        return false;
    if(run==length)
    {
        if(size_l(root)==0)
        {
            root = NULL;
            return true;
        }
        else
        {
            root->islast=False;
            return  false;
        }
    }
    else
    {
        int index = key[run]-'a';
        to_deleted = delete_word(key,root->children[index],length,run+1);
        if(to_deleted)
        {
            
        }
    }
    return  true;
}
void no_of_words(TrieNode* root,int& ans)
{
    if(!root)
        return;
    if(root->islast)
    {
        ans=ans+1;
    }
    for(auto child:root->children)
    {
        if(child)
        {
            no_of_words(child,ans);
        }
    }
}
void print(TrieNode* root)
{
    if(!root)
    {
        return;
    }
    cout<<root->ch<<" ";
    for(auto child : root->children)
    {
        if(child)
        {
            print(child);
        }
    }
}
void helper(TrieNode* root,vector<string>& ans,string s1)
{
    if(!root)
        return;
    if(root->islast)
    {
        s1=s1+root->ch;
        ans.push_back(s1);
    }
    for(auto child : root->children)
    {
        if(child)
        {
            s1 = s1+root->ch;
            helper(child,ans,s1);
        }   
    }
}
vector<string> words_in_trie(TrieNode* root)
{
    vector<string> ans;
    string s1="";
    helper(root,ans,s1);
    return ans;
}
int main()
{
    TrieNode* t1 = new TrieNode('a');
    string a = "ryan";
    string a1 = "run";
    insert(t1,a);
    insert(t1,a1);
    print(t1);
    int ans=0;
    no_of_words(t1,ans);
    cout<<ans<<endl;
    cout<<search(t1,"aryan")<<endl;
    vector<string> ans1 = words_in_trie(t1);
    for(int i=0; i<ans1.size(); i++)
    {
        cout<<ans1[i]<<endl;
    }
}