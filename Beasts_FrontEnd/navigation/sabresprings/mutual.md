---
layout: post 
show_reading_time: false
title: Mutual Schedule
permalink: /sabresprings/mutual
description: Here are the activities. Hover over image for more details
---

<style>
{{ '@import "beasts/inline/navigation/navigation-sabresprings-activity-1";' | scssify }}
</style>

## Winter ❄️
<!-- SECTION 1: Winter options -->
<div id="winter_container"></div>

## Spring 🌸
<!-- SECTION 2: Spring options -->
<div id="spring_container"></div>

## Summer ☀️
<!-- SECTION 3: Summer Options -->
<div id="summer_container"></div>

## Fall 🍂
<!-- SECTION 4: Fall Options -->
<div id="fall_container"></div>

<script>
{
  // Function to create activity grid
  function createActivityGrid(containerId, activities) {
    const outputElement = document.getElementById(containerId);
    outputElement.innerHTML = '';

    const container = document.createElement('div');
    container.className = 'activity-grid';

    for (const activity of activities) {
      const item = document.createElement('div');
      item.className = 'activity-item';

      // Handle single or dual images
      if (activity.image2) {
        const dualContainer = document.createElement('div');
        dualContainer.className = 'dual-images';
        
        const img1 = document.createElement('img');
        img1.src = activity.image;
        img1.alt = activity.title;
        
        const img2 = document.createElement('img');
        img2.src = activity.image2;
        img2.alt = activity.title;
        
        dualContainer.appendChild(img1);
        dualContainer.appendChild(img2);
        item.appendChild(dualContainer);
      } else {
        const img = document.createElement('img');
        img.src = activity.image;
        img.alt = activity.title;
        item.appendChild(img);
      }

      const title = document.createElement('div');
      title.className = 'title';
      title.textContent = activity.title;

      const shortDesc = document.createElement('div');
      shortDesc.className = 'short-desc';
      shortDesc.textContent = activity.shortDesc;

      const dateElem = document.createElement('div');
      dateElem.className = 'date';
      if (activity.date) {
        dateElem.textContent = activity.date;
      }

      const hoverDesc = document.createElement('div');
      hoverDesc.className = 'hover-desc';
      hoverDesc.textContent = activity.hoverDesc;

      //item.appendChild(img);
      item.appendChild(title);
      item.appendChild(shortDesc);
      if (activity.date) {
        item.appendChild(dateElem);
      }
      item.appendChild(hoverDesc);

      container.appendChild(item);
    }

    outputElement.appendChild(container);
  }
  
  // Winter Activities (December - February)
  const winterActivities = [
    {
      image: "https://images.squarespace-cdn.com/content/v1/60e757f61b4744152aa1a2ca/1632353049852-ZWKE37RF6HWIUK5MPXKD/%23edf7fb.png?format=1500w",
      title: "Yogurt and Planning",
      shortDesc: "In the Mix, Hover for Link",
      hoverDesc: "Come with the 'what do I want to do' mindset: https://www.inthemixyogurt.com/",
      date: "Jan 27 - Offiste 7:30PM"
    },
    {
      image: "https://upload.wikimedia.org/wikipedia/commons/e/ec/Soccer_ball.svg",
      image2: "https://upload.wikimedia.org/wikipedia/commons/3/3e/Tennis_Racket_and_Balls.jpg",
      title: "Soccer and Tennis",
      shortDesc: "Play Ball",
      hoverDesc: "Combined activity with Priests and Teachers",
      date: "Feb 3 - Church"
    },
    {
      image: "https://www.churchofjesuschrist.org/imgs/5288eedbc6e58a3ad9d586eb850d926a7d30ab5a/full/1280%2C/0/default",
      title: "Temple Trip",
      shortDesc: "Come enter The Lord's House",
      hoverDesc: "We are blessed to have a temple so close, as we prepare for the San Diego Open House soon.",
      date: "Sat Feb 14 - Newport Beach"
    },
    {
      image: "https://upload.wikimedia.org/wikipedia/commons/thumb/7/79/Fotograf%C3%ADa_de_taller.jpg/2560px-Fotograf%C3%ADa_de_taller.jpg",
      title: "Basic Automotive",
      shortDesc: "Car Basics",
      hoverDesc: "Learn fundamental automotive skills: checking oil, changing tires, and understanding how cars work!",
      date: "Feb 24 - Church"
    },
  ];
  
  // Spring Activities (March - May)
  const springActivities = [
    {
      image: "https://upload.wikimedia.org/wikipedia/commons/6/61/Overgrown_yard_-_geograph.org.uk_-_964505.jpg",
      title: "Yard Cleanup",
      shortDesc: "Bless Your Fellow Man",
      hoverDesc: "Help someone in the community with spring yard cleanup. Service project with lunch included!",
      date: "May 5 - Church"
    },
    {
      image: "https://upload.wikimedia.org/wikipedia/commons/thumb/2/2a/A_simple_campfire.jpg/2560px-A_simple_campfire.jpg",
      image2: "https://upload.wikimedia.org/wikipedia/commons/5/5e/Coleman_stove.jpg",
      title: "Camping & Outdoors Activities",
      shortDesc: "Outdoor Adventure",
      hoverDesc: "Setup camp, learn campfire safety, how to cook delicious meals in nature, hiking, milling, offroad, and how to enjoy the great outdoors under the stars!",
      date: "Saturday May 23 - Julian"
    },
  ];
  
  // Summer Activities (June - August)
  const summerActivities = [
    {
      image: "{{site.baseurl}}/images/activity/planofhappygame.png",
      title: "Video Game Making",
      shortDesc: "Plan of Happiness",
      hoverDesc: "Create your own video game with a positive message! Learn basic game design and coding.",
      date: "Aug 18 - Spring Meadow Lane"
    }
  ];
  
  // Fall Activities (September - November)
  const fallActivities = [
    {
      image: "{{site.baseurl}}/images/activity/frisbeegolf.png",
      title: "Frisbee Golf",
      shortDesc: "Modified Sport",
      hoverDesc: "Play disc golf on a custom course! Great outdoor activity combining skill and fun."
    },
  ];
  
  // Create all grids
  createActivityGrid('winter_container', winterActivities);
  createActivityGrid('spring_container', springActivities);
  createActivityGrid('summer_container', summerActivities);
  createActivityGrid('fall_container', fallActivities);
}
</script>

---
