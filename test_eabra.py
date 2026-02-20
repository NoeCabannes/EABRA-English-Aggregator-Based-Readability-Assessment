from eabra.pipeline import EABRAPipeline
import pandas as pd

def main():
    print("Initializing EABRA Pipeline MVP...")
    pipeline = EABRAPipeline()
    
    # Sample texts: One simple (children's story like), one complex (news article)
    text1 = "The cat sat on the mat. It was a very nice mat. The cat liked the mat."
    text2 = "Concurrently, the economic ramifications of implementing such a substantial quantitative easing program are profound, significantly altering the macroeconomic landscape."
    
    df = pd.DataFrame({'text_id': [1, 2], 'text': [text1, text2]})
    
    print("Processing DataFrame...")
    results_df = pipeline.process_dataframe(df, 'text')
    
    print("\nExtraction Complete! Found {} feature columns.".format(len(results_df.columns) - 2))
    
    print("\nFull output for Text 1 and Text 2:")
    
    for col in results_df.columns:
        if col not in ['text_id', 'text']:
            val1 = results_df.iloc[0][col]
            val2 = results_df.iloc[1][col]
            if isinstance(val1, float):
                print(f"{col:25s}: Text 1 = {val1:7.2f} | Text 2 = {val2:7.2f}")
            else:
                print(f"{col:25s}: Text 1 = {str(val1):>7s} | Text 2 = {str(val2):>7s}")
            
if __name__ == "__main__":
    main()
