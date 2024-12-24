// Link: https://leetcode.com/problems/max-chunks-to-make-sorted/
function maxChunksToSorted(arr: number[]): number {
    let chunks=0;
    const sums:number[]=[];
      for(let i=0;i<arr.length;i++){
        let sumNi=0;
        for(let j=0;j<i+1;j++){
            sumNi+=arr[j];
        }
        sums.push(sumNi);    
      }
      for(let i=0;i<arr.length;i++){
        if(sums[i]===(i*(i+1)/2)) chunks++;
      }
       return chunks
       }
    