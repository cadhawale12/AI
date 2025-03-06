{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "141f29a6-9783-4097-bdb2-f8152aac730a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "* Running on local URL:  http://127.0.0.1:7860\n",
      "\n",
      "To create a public link, set `share=True` in `launch()`.\n"
     ]
    },
    {
     "data": {
      "text/html": [
       "<div><iframe src=\"http://127.0.0.1:7860/\" width=\"100%\" height=\"500\" allow=\"autoplay; camera; microphone; clipboard-read; clipboard-write;\" frameborder=\"0\" allowfullscreen></iframe></div>"
      ],
      "text/plain": [
       "<IPython.core.display.HTML object>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/plain": []
     },
     "execution_count": 1,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import gradio as gr\n",
    "\n",
    "def greet(name):\n",
    "    return \"Hello \" + name + \"!!\"\n",
    "\n",
    "demo = gr.Interface(fn=greet, inputs=\"text\", outputs=\"text\")\n",
    "demo.launch()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a73b2376-87d7-4150-b2c5-d41ee1214480",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
