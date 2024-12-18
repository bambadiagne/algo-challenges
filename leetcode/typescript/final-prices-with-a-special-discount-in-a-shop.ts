// Link: https://leetcode.com/problems/final-prices-with-a-special-discount-in-a-shop/description/
function finalPrices(prices: number[]): number[] {
    const answers=prices.slice();
    for(let i=0;i<prices.length;i++ ){
      let j=i+1;
      while(j<prices.length){
          if(prices[j]<=prices[i]){
               answers[i]=prices[i]-prices[j];
              break;
          }
          j++;
      }
    }
  return answers
  };