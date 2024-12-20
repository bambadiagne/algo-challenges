// Link: https://leetcode.com/problems/jewels-and-stones/
function numJewelsInStones(jewels: string, stones: string): number {
    let count=0;
    const mapJewels:Record<string,string>={
        
    }
    for(let i=0;i<jewels.length;i++){
        mapJewels[jewels[i]]=jewels[i];   
    }
    for(let i=0;i<stones.length;i++){
        if(mapJewels[stones[i]]) count++;
    }
    return count;
};